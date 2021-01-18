# -*- coding: UTF-8 -*-
from actors import *
import random
import xlrd
# 打开文件
data = xlrd.open_workbook('input.xlsx')
# 查看工作表
data.sheet_names()
# 通过文件名获得工作表,获取工作表1
table = data.sheet_by_name('Sheet1')
table2= data.sheet_by_name('Sheet2')
rows = table.nrows # 弟子总的行数
columns = table.ncols # 弟子总的列数
rows2 = table2.nrows # 敌人总的行数
columns2 = table2.ncols # 敌人总的列数
def main():
    enemy_class=[]
    player_class=[]
    for i in range(1,rows):
        name, strength, talent, speed, spirit, chance, evade, defense=table.row_values(i)[1:]
        player=Player(name, strength, talent, speed, spirit, chance, evade, defense) 
        player_class.append(player)
    for i in range(1,rows2):
        name, strength, talent, speed, spirit, chance, evade, defense=table2.row_values(i)[1:]
        enemy=Enemy(name, strength, talent, speed, spirit, chance, evade, defense) 
        enemy_class.append(enemy)
    gameon=1
    print("参战弟子: ")
    print(player_class)
    print("参战敌人: ")
    print(enemy_class)
    
    
    def removedead(player_class,enemy_class,gameon):
        for i in range(len(player_class) -1, -1, -1):
                if player_class[i].hp <= 0: 
                    print("弟子"+player_class[i].name+"阵亡。")
                    player_class.pop(i)
                    if player_class==[]: print("弟子全体阵亡。")
                    else:
                        print("现在弟子还剩: ")
                        print(player_class)
                    if len(player_class)<=0: 
                        gameon=0
                        return gameon
                    continue
                if len(player_class)<=0: break
        for i in range(len(enemy_class) -1, -1, -1):
            if enemy_class[i].hp <= 0: 
                print("敌人"+enemy_class[i].name+"阵亡。")
                enemy_class.pop(i)
                if enemy_class==[]: print("敌人全体阵亡。")
                else:
                    print("现在敌人还剩: ")
                    print(enemy_class)
                if len(enemy_class)<=0: 
                    gameon=0
                    return gameon
                continue
            if len(enemy_class)<=0: break
           
    
    while len(player_class) > 0 and len(enemy_class) > 0 and gameon==1:
        try:    
            for i in range(len(player_class) ):
                player_class[i].update()
                player_class[i].attack(enemy_class[random.randint(0, len(enemy_class) - 1)],enemy_class, gameon)
                removedead(player_class,enemy_class,gameon)
                if gameon==0: break
            if gameon==0: break
            for i in range(len(enemy_class)):
                enemy_class[i].update()
                enemy_class[i].attack(player_class[random.randint(0, len(player_class) - 1)],player_class, gameon)
                removedead(player_class,enemy_class,gameon)
                if gameon==0: break
            if gameon==0: break
        except: 
            break    
    print("运行结束")
    if enemy_class==[]: print("我方获胜")
    else: print("敌方获胜")
    
if __name__ == '__main__': #加入main函数用于测试程序 #协调入口（从哪个代码开始执行）
    main()