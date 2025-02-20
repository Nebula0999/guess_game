import random
from django.shortcuts import render


male_facts = [
    "Men in their 20's often focus on building their careers.",
    "Many men in their 20's enjoy outdoor activities like hiking and sports.",
    "Men in their 20's are more likely to take risks.",
    "Men in their 20's often prioritize fitness and health.",
    "Many men in their 20's are exploring their passions and hobbies.",
    "Men in their 20's are often tech-savvy and interested in gadgets.",
    "Men in their 20's are more likely to travel and explore new places.",
    "Men in their 20's often value friendships and social connections.",
    "Men in their 20's are more likely to experiment with different styles.",
    "Men in their 20's are often focused on personal growth and self-improvement."
    "Most young men in their 20's are obsessed with sneakers and have at least one pair they never wear.",
    "Many young men in their 20's secretly enjoy cooking but pretend they only know how to make instant noodles.",
    "In their 20's, young men often have a playlist for every mood, from gym workouts to late-night chill sessions.",
    "Most young men in their 20's have a hidden talent they only show off at parties, like beatboxing or dancing.",
    "Many young men in their 20's dream of starting a business but are still figuring out how to save money.",
    "Young men in their 20's are experts at turning random ingredients into a surprisingly tasty meal.",
    "Most young men in their 20's have a favorite sports team they defend passionately, even if the team is losing.",
    "In their 20's, young men often have a love-hate relationship with early mornings and late-night gaming sessions.",
    "Many young men in their 20's are secretly into skincare but won't admit it to their friends.",
    "Young men in their 20's are always on the lookout for the next big thing, whether it's a gadget, app, or trend."
]

female_facts = [
    "Women in their 20's often balance career and personal life.",
    "Many women in their 20's are passionate about health and wellness.",
    "Women in their 20's are more likely to pursue higher education.",
    "Women in their 20's often enjoy creative hobbies like painting or writing.",
    "Many women in their 20's are focused on building strong relationships.",
    "Women in their 20's are often interested in fashion and beauty trends.",
    "Women in their 20's are more likely to prioritize mental health.",
    "Women in their 20's often enjoy traveling and exploring new cultures.",
    "Women in their 20's are often tech-savvy and active on social media.",
    "Women in their 20's are often focused on achieving financial independence."
    "Most young girls in their 20's have a secret stash of snacks they don't share with anyone.",
    "Many young girls in their 20's are experts at multitasking, like studying while binge-watching their favorite show.",
    "In their 20's, young girls often have a favorite lipstick or lip gloss they can't leave the house without.",
    "Most young girls in their 20's have a folder of memes they save for the perfect moment to share.",
    "Many young girls in their 20's are passionate about self-care and have a skincare routine they swear by.",
    "Young girls in their 20's are always on the lookout for the next viral TikTok trend to try out.",
    "Most young girls in their 20's have a playlist for every occasion, from road trips to heartbreak recovery.",
    "In their 20's, young girls often have a favorite coffee order they customize to perfection.",
    "Many young girls in their 20's are secretly planning their dream wedding while pretending they're too cool for it.",
    "Young girls in their 20's are experts at finding the best deals online and will spend hours hunting for discounts."
]

import gender_guesser.detector as gender
import random

def guess_gender(request):
    d = gender.Detector()
    if request.method == 'POST':
        name = request.POST.get('name', '').strip().capitalize()
        gender_result = d.get_gender(name)

        if gender_result in ['male', 'mostly_male']:
            fact = random.choice(male_facts)
            gender_display = "male"
        elif gender_result in ['female', 'mostly_female']:
            fact = random.choice(female_facts)
            gender_display = "female"
        else:
            fact = "Sorry, we couldn't determine the gender based on the name."
            gender_display = "unknown"

        return render(request, 'game/result.html', {'name': name, 'gender': gender_display, 'fact': fact})
    return render(request, 'game/index.html')

# Create your views here.
