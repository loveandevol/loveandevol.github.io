public class GetCircle{
	public static void main(String args[]){
		Circle circle0;
		Circle circle1;
		circle0=new Circle();
		circle1=new Circle(3);
		System.out.println("面积: "+circle0.getArea());
		System.out.println("周长: "+circle0.getLength());
		System.out.println("面积: "+circle1.getArea());
		System.out.println("周长: "+circle1.getLength());
	}
}
