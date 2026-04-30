#ifndef GOT_HPP
#define GOT_HPP

class Character {
public:
    Character(); // basic constructor
    Character(int h, int dm, int d); // set values for constructor
    int getHealth();
    int getmaxHealth();
    int getDMG();           // get functions
    int getDEF();
    int getBlock();
    void takeDMG(int dmgTaken);   // applys dmg
    void startTurn(); // resets block
    void addBlock(int amount); 
    int isAlive(); // checks if alive
    




private:
    int health;
    int maxHealth;
    int dmg;
    int def;
    int block;
};














#endif