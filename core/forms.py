from django import forms

# Choices for answers
AGREEMENT_CHOICES = [
    (1, "Pas du tout d'accord"),
    (2, "Plutôt pas d'accord"),
    (3, "Neutre"),
    (4, "Plutôt d'accord"),
    (5, "Tout à fait d'accord"),
]

FREQUENCY_CHOICES = [
    (1, "Jamais"),
    (2, "Rarement"),
    (3, "Parfois"),
    (4, "Souvent"),
    (5, "Très souvent"),
]

class MentalHealthForm(forms.Form):
    # --- Big Five Personality Test ---
    # Openness
    openness_1 = forms.ChoiceField(label="Je suis plein d'idées.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    openness_2 = forms.ChoiceField(label="J'ai une imagination vive.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    openness_3 = forms.ChoiceField(label="Je suis curieux(se) de nombreuses choses.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    openness_4 = forms.ChoiceField(label="J'ai une imagination active.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    openness_5 = forms.ChoiceField(label="Je préfère un travail routinier.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)

    # Conscientiousness
    conscientiousness_1 = forms.ChoiceField(label="Je suis toujours bien préparé(e).", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    conscientiousness_2 = forms.ChoiceField(label="Je fais attention aux détails.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    conscientiousness_3 = forms.ChoiceField(label="Je fais rapidement les tâches ménagères.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    conscientiousness_4 = forms.ChoiceField(label="Je respecte un planning.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    conscientiousness_5 = forms.ChoiceField(label="Je mets du désordre dans mes affaires.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)

    # Extraversion
    extraversion_1 = forms.ChoiceField(label="Je suis le/la boute-en-train de la fête.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    extraversion_2 = forms.ChoiceField(label="Je parle à beaucoup de personnes lors de fêtes.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    extraversion_3 = forms.ChoiceField(label="Je me sens à l'aise avec les gens.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    extraversion_4 = forms.ChoiceField(label="Je démarre des conversations.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    extraversion_5 = forms.ChoiceField(label="Je n'aime pas attirer l'attention sur moi.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)

    # Agreeableness
    agreeableness_1 = forms.ChoiceField(label="Je m'intéresse aux autres.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    agreeableness_2 = forms.ChoiceField(label="Je compatis aux sentiments des autres.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    agreeableness_3 = forms.ChoiceField(label="J'ai un cœur tendre.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    agreeableness_4 = forms.ChoiceField(label="Je consacre du temps aux autres.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    agreeableness_5 = forms.ChoiceField(label="Je ressens peu de souci pour les autres.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)

    # Neuroticism
    neuroticism_1 = forms.ChoiceField(label="Je suis facilement stressé(e).", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    neuroticism_2 = forms.ChoiceField(label="Je m'inquiète souvent.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    neuroticism_3 = forms.ChoiceField(label="Je suis facilement perturbé(e).", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    neuroticism_4 = forms.ChoiceField(label="Je me mets facilement en colère.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)
    neuroticism_5 = forms.ChoiceField(label="Je change souvent d'humeur.", choices=AGREEMENT_CHOICES, widget=forms.RadioSelect)

    # --- Maslach Burnout Inventory (MBI) ---
    emotional_exhaustion_1 = forms.ChoiceField(label="Je me sens vidé(e) émotionnellement par mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    emotional_exhaustion_2 = forms.ChoiceField(label="Je me sens épuisé(e) à la fin de ma journée de travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    emotional_exhaustion_3 = forms.ChoiceField(label="Je me sens fatigué(e) en me levant pour aller travailler.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    emotional_exhaustion_4 = forms.ChoiceField(label="Je me sens frustré(e) par mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    emotional_exhaustion_5 = forms.ChoiceField(label="Je suis à bout de nerfs au travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    depersonalization_1 = forms.ChoiceField(label="Je traite certains bénéficiaires comme des objets impersonnels.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    depersonalization_2 = forms.ChoiceField(label="Je suis devenu(e) plus insensible envers les gens.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    depersonalization_3 = forms.ChoiceField(label="Ce travail m'endurcit émotionnellement.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    depersonalization_4 = forms.ChoiceField(label="Je me préoccupe peu de ce qui arrive aux bénéficiaires.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    personal_accomplishment_1 = forms.ChoiceField(label="Je pense avoir une influence positive sur la vie des gens.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    personal_accomplishment_2 = forms.ChoiceField(label="Je me sens énergique.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    personal_accomplishment_3 = forms.ChoiceField(label="Je comprends facilement les bénéficiaires.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    personal_accomplishment_4 = forms.ChoiceField(label="Je résous efficacement les problèmes des bénéficiaires.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    # --- Karasek Job Strain Model ---
    psychological_demands_1 = forms.ChoiceField(label="Mon travail exige de travailler très vite.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    psychological_demands_2 = forms.ChoiceField(label="Mon travail demande de travailler très dur.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    psychological_demands_3 = forms.ChoiceField(label="Je dois respecter des délais serrés.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    psychological_demands_4 = forms.ChoiceField(label="Je dois me concentrer intensément pendant de longues périodes.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    skill_discretion_1 = forms.ChoiceField(label="Mon travail m'oblige à apprendre de nouvelles choses.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    skill_discretion_2 = forms.ChoiceField(label="Mon travail est très répétitif.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    skill_discretion_3 = forms.ChoiceField(label="J'ai l'occasion de développer mes compétences.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    skill_discretion_4 = forms.ChoiceField(label="Mon travail est varié.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    decision_authority_1 = forms.ChoiceField(label="J'ai beaucoup à dire sur ce qui se passe dans mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    decision_authority_2 = forms.ChoiceField(label="J'ai la liberté de décider comment je fais mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)

    social_support_1 = forms.ChoiceField(label="Mon superviseur m'aide à faire mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    social_support_2 = forms.ChoiceField(label="Mes collègues m'aident à faire mon travail.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    social_support_3 = forms.ChoiceField(label="Je peux compter sur mes collègues en cas de problème.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)
    social_support_4 = forms.ChoiceField(label="Je peux compter sur mon superviseur en cas de problème.", choices=FREQUENCY_CHOICES, widget=forms.RadioSelect)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
