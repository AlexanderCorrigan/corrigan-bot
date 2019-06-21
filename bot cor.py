import vk_api

vk = vk.api.VkApi(token = "be7bbac1a59df6f13ecf39cce7c76b42c8dfb2fd4453cfb79bf37e1ef4a8573cf84c53f0802942070a9b7")

while True:
    messages = vk.method("messages.getConversations", {"offset":0, "count":20, "filter": "inread"})
    if messages["count"] >=1:
        id = messages["items"][0]["last_message"]["from_id"]
        body = messages["items"][0]["last_message"]["text"]
        if body.lower() == "привет":
            vk.method("messages.send", {"peer_id":id, "message":"Привет!"})
        elif body.lower() == "Как дела?":
            vk.method("messade.send", {"peer_id":id, "message":"Нормально, ты как?"})
        else:
            vk.method("messade.send", {"peer_id": id, "message": "Я не понял тебя."})
        tune.sleep(1)