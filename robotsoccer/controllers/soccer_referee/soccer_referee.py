from controller import Supervisor

supervisor = Supervisor()

timestep = int(supervisor.getBasicTimeStep())

ball_solid = supervisor.getFromDef("BALL")
trans_field = ball_solid.getField("translation")


    

while supervisor.step(timestep) != -1:

    values = trans_field.getSFVec3f()
    print("Ball position: %g %g %g" % (values[0], values[1], values[2]))
    
    if(-0.75 < values[2] < 0.75):
        if( -4.5 > values[0] or 4.5 < values[0]):
            trans_field.setSFVec3f([0,0,0])
            ball_solid.resetPhysics()
    elif(values[0] < -4.5):
         trans_field.setSFVec3f([values[0] + 0.113, values[1], values[2]])
         ball_solid.resetPhysics()
    elif(values[0] > 4.5):
         trans_field.setSFVec3f([values[0] - 0.113, values[1], values[2]])
         ball_solid.resetPhysics()
    
    if(values[2] > 3):
        trans_field.setSFVec3f([values[0], values[1], (values[2] - 0.113)])
        ball_solid.resetPhysics()
    if(values[2] < -3):
        trans_field.setSFVec3f([values[0], values[1], (values[2] + 0.113)])
        ball_solid.resetPhysics()

       

        
        
