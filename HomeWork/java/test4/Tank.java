public class Tank{
	double speed;
	int bulletAmount;
	void speedUp(int s){
		speed=speed+s;
	}
	void speedDown(int d){
		if(speed-d>=0)
			speed=speed-d;
	}
	void setBulletAmount(int m){
		bulletAmount=m;
	}
	int getBulletAmount(){
		return bulletAmount;
	}
	double getSpeed(){
		return speed;
	}
	void fire(){
		if(bulletAmount>=1){
			bulletAmount--;
			System.out.println("打出一发炮弹");
		}
		else{
			System.out.println("没有炮弹,无法开火");
		}
	}
}
