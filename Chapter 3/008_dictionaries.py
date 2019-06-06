Nomad = {'type':'rover','color':'black','processor':'Jetson TX1'}

print(Nomad['type'])

BARB = {'type':'test-bed','color':'black','type':'wheeled'}

myRobots = {'BARB':'WIP','Nomad':Nomad,'Llamabot':'WIP'}

myRobots['Llamabot'] = 'Getting to it'

del myRobots['Llamabot']

workingRobots = myRobots.copy()

otherRobots = {'Rasbot-pi':'Pi-bot from book','spiderbot':'broken'}

myRobots.update(otherRobots)
