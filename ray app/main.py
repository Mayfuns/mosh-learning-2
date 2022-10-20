#UU37W7-ETRYX3VR45
# import wolframalpha for project
import wolframalpha

# this is an app id
app_id = 'UU37W7-ETRYX3VR45'

client = wolframalpha.Client(app_id)

ray = client.query('weather in lagos')

#print(ray)

answer = next(ray.results).text
print(answer)

#for ade in ray.pods:
    #for mainAnswer in ade.subpods:
        #print(mainAnswer.plaintext)