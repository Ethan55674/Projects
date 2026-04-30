#include <iostream>
#include "GOT.hpp"
#include <random>
std::random_device rd;
std::mt19937 gen(rd());

int enemyChoice(){
    std::uniform_int_distribution<int> dist(0,99);
    int roll = dist(gen);
    if (roll < 70){
        return 0;   // attack for enemy
    }
    else{
        return 1; // def will add more skills later
    }
    
}


int main(){
    Character player(25,6,6);
    Character enemy(15,3,5);
    std::cout << "YOUR HEALTH: " << player.getHealth() << " ENEMIES HEALTH: " << enemy.getHealth() << std::endl;
    while (player.isAlive() && enemy.isAlive()){
        int choice; 
        // player turn
        std::cout << "choice 1: ATTACK choice 2: DEFEND" << std::endl;
        std::cout.flush();
        std::cin >> choice;
        if (choice == 1){
            int damage = player.getDMG();
            enemy.takeDMG(damage);
        }
        else if (choice == 2){
            player.addBlock(player.getDEF());

        }
        if (!enemy.isAlive()){
            std::cout << "YOU WIN!!!!" << std::endl;
            break;
        }
        // now the enemies turn
        int enemy_choice = enemyChoice();
        if (enemy_choice == 0){
            std::cout << "THE ENEMY ATTACKS" << std::endl;
            int enemyDMG = enemy.getDMG();
            player.takeDMG(enemyDMG);
            std::cout << "YOUR HEALTH: " << player.getHealth() << " ENEMIES HEALTH: " << enemy.getHealth() << std::endl;
        }
        else if (enemy_choice == 1){
            std::cout << "THE ENEMY DEFENDS" << std::endl;
            enemy.addBlock(enemy.getDEF());
        }
        if (!player.isAlive()){
            std::cout << "YOU LOSE" << std::endl;
            break;
        }
        std::cout << "YOUR HEALTH: " << player.getHealth() << " ENEMIES HEALTH: " << enemy.getHealth() << std::endl;
        player.startTurn();
        enemy.startTurn();
    }
    return 0;
}