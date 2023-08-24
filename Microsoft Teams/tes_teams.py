import pymsteams

# Source 1: https://towardsdatascience.com/automate-teams-with-your-first-python-alerting-bot-bcc8f7c6ee5a
# Source 2 : https://stackoverflow.com/questions/59371631/send-automated-messages-to-microsoft-teams-using-python

myTeamsMessage = pymsteams.connectorcard("<link connector yang di copy dari microsoft teams>")
myMessageSection = pymsteams.cardsection()

# Section Title
myMessageSection.title("Section title")

# Activity Elements
myMessageSection.activityTitle("my activity title")
myMessageSection.activitySubtitle("my activity subtitle")
myMessageSection.activityImage("http://i.imgur.com/c4jt321l.png")
myMessageSection.activityText("This is my activity Text")

# Facts are key value pairs displayed in a list.
myMessageSection.addFact("this", "is fine")
myMessageSection.addFact("this is", "also fine")
myTeamsMessage.addSection(myMessageSection)
myTeamsMessage.text("Some Message")
myTeamsMessage.send()

# import pkg_resources
# installed_packages = pkg_resources.working_set
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#    for i in installed_packages])
# print(installed_packages_list)