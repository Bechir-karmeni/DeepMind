from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_big5_report(openness, conscientiousness, extraversion, agreeableness, neuroticism):
    report = []

    report.append("🔵 Résultats Big Five :")
    if openness > 7:
        report.append("Grande ouverture d'esprit : vous êtes créatif(ve) et curieux(se).")
    else:
        report.append("Faible ouverture d'esprit : vous êtes plutôt conventionnel(le).")

    if conscientiousness > 7:
        report.append("Haute conscienciosité : vous êtes organisé(e) et fiable.")
    else:
        report.append("Faible conscienciosité : vous aimez improviser et êtes flexible.")

    if extraversion > 7:
        report.append("Extraverti(e) : vous êtes sociable et énergique.")
    else:
        report.append("Introverti(e) : vous êtes plus réservé(e) et introspectif(ve).")

    if agreeableness > 7:
        report.append("Haut en agréabilité : vous êtes empathique et coopératif(ve).")
    else:
        report.append("Faible en agréabilité : vous êtes plus direct(e) et compétitif(ve).")

    if neuroticism > 7:
        report.append("Niveau élevé de neuroticisme : vous êtes plus sensible au stress.")
    else:
        report.append("Niveau faible de neuroticisme : vous êtes émotionnellement stable.")

    return report

def generate_mbi_report(mbi_score):
    report = []
    report.append("🧠 Résultat Burnout MBI :")
    if mbi_score > 7:
        report.append("Risque élevé de burnout détecté. ⚠️")
    elif mbi_score > 4:
        report.append("Burnout modéré : soyez attentif(ve) à vos symptômes.")
    else:
        report.append("Pas de signes importants de burnout. ✅")
    return report

def generate_karasek_report(demand, control, support):
    report = []
    report.append("⚙️ Résultat Stress Travail (Karasek) :")

    if demand > 7 and control < 4:
        report.append("Job strain élevé : beaucoup d'exigences, peu de contrôle.")
    elif demand > 7 and control > 6:
        report.append("Travail actif : exigence élevée mais autonomie élevée.")
    elif demand < 4 and control < 4:
        report.append("Travail passif : peu d'exigences, peu d'autonomie.")
    else:
        report.append("Travail détendu : équilibre satisfaisant entre exigences et contrôle.")

    if support < 5:
        report.append("Attention : faible soutien social au travail.")
    else:
        report.append("Bon niveau de soutien social.")

    return report

def generate_pdf(report_lines):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    p.setFont("Helvetica-Bold", 16)
    p.drawString(50, height - 50, "🧠 Résultats Psychométriques Personnalisés")

    p.setFont("Helvetica", 12)
    y = height - 100
    for line in report_lines:
        if y < 50:
            p.showPage()
            y = height - 50
        p.drawString(50, y, line)
        y -= 20

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer
