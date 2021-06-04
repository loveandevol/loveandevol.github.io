public class Circle{
	double radius;
	Circle(){
		radius=1;
	}
	Circle(double r){
		radius=r;
	}
	double getArea(){
		return 3.1415926*radius*radius;
	}
	double getLength(){
		return 2*3.1415926*radius;
	}
}
