import tweepy
#Authentication twitter
auth=tweepy.OnAuthHandler("pGBDoAaEpkliVKB0LwjtcmHGc","xF3g1wrP50b6B1ZEd20u40VfjgH1FGQcuWUz1Q05aUWOufv1hw")
auth.set_access_token("622518493-6VcLIPprbQbv9wkcBBPvCle8vsjU9fE85Dq9oStl", 
    "tH9aKQbQQ1iRdYTcLSsPwitl44BkAc6jilrsU0ifnXvZhq")
api=tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error durring authentication")
