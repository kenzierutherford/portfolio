#include <Servo.h>

Servo servoLeft;

void setup() 

  {
    servoLeft.attach(13);
    servoLeft.writeMicroseconds(1500);
}
void loop() {
void forward(void)
        { 
          analogWrite(EA,254); //speed 0 - 255
          analogWrite(EB,255); //speed 0 - 255
          digitalWrite(EN2,LOW);
          digitalWrite(EN3,HIGH);
          digitalWrite(EN4,LOW);
          digitalWrite(EN5,HIGH);
        }
void backward(void)
        {        
          analogWrite(EA,255);//speed 0 - 255
          analogWrite(EB,255); //speed 0 - 255 
          digitalWrite(EN2,HIGH);
          digitalWrite(EN3,LOW);
          digitalWrite(EN4,HIGH);
          digitalWrite(EN5,LOW);            
        }
void left(void)
        {        
          analogWrite(EA,180); //speed 0 - 255
          analogWrite(EB,180); //speed 0 - 255
          digitalWrite(EN2,LOW);
          digitalWrite(EN3,HIGH);
          digitalWrite(EN4,HIGH);
          digitalWrite(EN5,LOW);     
        }        
void right(void)
}       
          analogWrite(EA,180);//speed 0 - 255
          analogWrite(EB,180); //speed 0 - 255
          digitalWrite(EN2,HIGH);
          digitalWrite(EN3,LOW);
          digitalWrite(EN4,LOW);
          digitalWrite(EN5,HIGH);

        }              
}

