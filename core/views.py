import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse, FileResponse
from django.db.models import Avg, Count

from .forms import MentalHealthForm
from .models import AnonymousSubmission
from .utils import generate_big5_report, generate_mbi_report, generate_karasek_report, generate_pdf

def employee_form(request):
    sector = request.GET.get('sector', 'Général')

    if request.method == 'POST':
        form = MentalHealthForm(request.POST)
        if form.is_valid():
            # ➡️ Big Five
            openness = (
                int(form.cleaned_data['openness_1']) +
                int(form.cleaned_data['openness_2']) +
                int(form.cleaned_data['openness_3']) +
                int(form.cleaned_data['openness_4']) +
                (6 - int(form.cleaned_data['openness_5']))
            ) / 5

            conscientiousness = (
                int(form.cleaned_data['conscientiousness_1']) +
                int(form.cleaned_data['conscientiousness_2']) +
                int(form.cleaned_data['conscientiousness_3']) +
                int(form.cleaned_data['conscientiousness_4']) +
                (6 - int(form.cleaned_data['conscientiousness_5']))
            ) / 5

            extraversion = (
                int(form.cleaned_data['extraversion_1']) +
                int(form.cleaned_data['extraversion_2']) +
                int(form.cleaned_data['extraversion_3']) +
                int(form.cleaned_data['extraversion_4']) +
                (6 - int(form.cleaned_data['extraversion_5']))
            ) / 5

            agreeableness = (
                int(form.cleaned_data['agreeableness_1']) +
                int(form.cleaned_data['agreeableness_2']) +
                int(form.cleaned_data['agreeableness_3']) +
                int(form.cleaned_data['agreeableness_4']) +
                (6 - int(form.cleaned_data['agreeableness_5']))
            ) / 5

            neuroticism = (
                int(form.cleaned_data['neuroticism_1']) +
                int(form.cleaned_data['neuroticism_2']) +
                int(form.cleaned_data['neuroticism_3']) +
                int(form.cleaned_data['neuroticism_4']) +
                int(form.cleaned_data['neuroticism_5'])
            ) / 5

            # ➡️ MBI
            mbi_score = (
                int(form.cleaned_data['emotional_exhaustion_1']) +
                int(form.cleaned_data['emotional_exhaustion_2']) +
                int(form.cleaned_data['emotional_exhaustion_3']) +
                int(form.cleaned_data['emotional_exhaustion_4']) +
                int(form.cleaned_data['emotional_exhaustion_5']) +
                int(form.cleaned_data['depersonalization_1']) +
                int(form.cleaned_data['depersonalization_2']) +
                int(form.cleaned_data['depersonalization_3']) +
                int(form.cleaned_data['depersonalization_4'])
            )

            # ➡️ Karasek
            karasek_demand = (
                int(form.cleaned_data['psychological_demands_1']) +
                int(form.cleaned_data['psychological_demands_2']) +
                int(form.cleaned_data['psychological_demands_3']) +
                int(form.cleaned_data['psychological_demands_4'])
            )

            karasek_control = (
                int(form.cleaned_data['skill_discretion_1']) +
                (6 - int(form.cleaned_data['skill_discretion_2'])) +
                int(form.cleaned_data['skill_discretion_3']) +
                int(form.cleaned_data['skill_discretion_4']) +
                int(form.cleaned_data['decision_authority_1']) +
                int(form.cleaned_data['decision_authority_2'])
            )

            karasek_support = (
                int(form.cleaned_data['social_support_1']) +
                int(form.cleaned_data['social_support_2']) +
                int(form.cleaned_data['social_support_3']) +
                int(form.cleaned_data['social_support_4'])
            )

            # 📝 Générer les rapports
            report_big5 = generate_big5_report(openness, conscientiousness, extraversion, agreeableness, neuroticism)
            report_mbi = generate_mbi_report(mbi_score)
            report_karasek = generate_karasek_report(karasek_demand, karasek_control, karasek_support)

            full_report = report_big5 + [""] + report_mbi + [""] + report_karasek

            # Enregistrement BDD
            AnonymousSubmission.objects.create(
                submission_id=str(uuid.uuid4()),
                phq9_score=0,
                gad7_score=0,
                mbi_score=mbi_score,
                combined_report="\n".join(full_report),
                sector=sector,
                has_quit=False
            )

            # Stocker dans session pour le PDF
            request.session['report_data'] = full_report

            return render(request, 'core/report.html', {'report': full_report})

    else:
        form = MentalHealthForm()

    return render(request, 'core/form.html', {'form': form})

# 🚀 Dashboard GRH
@login_required
def grh_dashboard(request):
    if not request.user.groups.filter(name='GRH').exists():
        return HttpResponse("Accès refusé : vous n'êtes pas GRH.", status=403)

    data = AnonymousSubmission.objects.all()
    labels = [str(entry.submission_id) for entry in data]
    scores = [entry.mbi_score for entry in data]

    avg_mbi = data.aggregate(Avg('mbi_score'))['mbi_score__avg'] or 0
    total_entries = data.count()

    high_risk = data.filter(mbi_score__gt=6).count()
    risk_percent = round((high_risk / total_entries) * 100, 2) if total_entries else 0
    quit_count = data.filter(has_quit=True).count()
    turnover_percent = round((quit_count / total_entries) * 100, 2) if total_entries else 0

    by_sector = data.values('sector').annotate(
        count=Count('id'),
        avg_mbi=Avg('mbi_score')
    )

    return render(request, 'core/dashboard.html', {
        'data': data,
        'labels': labels,
        'scores': scores,
        'avg_mbi': avg_mbi,
        'risk_percent': risk_percent,
        'turnover_percent': turnover_percent,
        'total_entries': total_entries,
        'by_sector': list(by_sector)
    })

# ✉️ Envoyer email
def send_invitation_email(email, name, sector='Général'):
    subject = "Invitation à remplir votre test psychométrique"
    message = f"""
Bonjour {name},

Merci de compléter ce formulaire confidentiel :
👉 http://localhost:8000/form/?sector={sector}

Ce questionnaire est totalement anonyme.

Merci.
"""
    from_email = "admin@mentalplatform.com"
    send_mail(subject, message, from_email, [email])

@login_required
def send_email_interface(request):
    if not request.user.groups.filter(name='GRH').exists():
        return HttpResponse("Accès refusé : vous n'êtes pas RH.", status=403)

    message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        sector = request.POST.get('sector', 'Général')
        send_invitation_email(email, name, sector)
        message = f"✅ Email envoyé à {name} ({email}) pour le secteur {sector}."

    return render(request, 'core/send_email.html', {'message': message})

# 🏡 Home redirect
def home_redirect(request):
    return redirect('/accounts/login/')

# 📥 Download Report PDF
def download_report_pdf(request):
    report = request.session.get('report_data')
    if not report:
        return HttpResponse("Aucun rapport disponible.", status=404)

    pdf_file = generate_pdf(report)
    return FileResponse(pdf_file, as_attachment=True, filename="rapport_test_personnalite.pdf")
