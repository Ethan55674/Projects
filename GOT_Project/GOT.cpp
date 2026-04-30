#include "GOT.hpp"
#include <iostream>


// character class

Character::Character(int h, int dm, int d){
    this->health = h;
    this->dmg = dm;
    this->def = d;
}

int Character::getHealth(){
    return health;
}
int Character::getDMG(){
    return dmg;
}
int Character::getmaxHealth(){
    return maxHealth;
}
int Character::getDEF(){
    return def;
}
int Character::getBlock(){
    return block;
}
void Character::takeDMG(int dmgTaken){
    dmgTaken = (dmgTaken - block);
    if (dmgTaken > 0){ // this is for if the damage is higher than the block
        this->health -= dmgTaken;
    }
    else{ // this is for if the damage is less than the block
        std::cout << "you took no damage" << std::endl;
    }

}
void Character::startTurn(){
    block = 0;
}

void Character::addBlock(int amount){
    block += amount;
}
int Character::isAlive(){
    return health > 0;
}


// new class gonna do a 