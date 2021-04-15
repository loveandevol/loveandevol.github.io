public class Student extends Person{
	String major;
	String classes;
	Student(String name,
			char sex,
			int age,
			String major,
			String classes){
		super(name,sex,age);
		this.major=major;
		this.classes=classes;
	}
	void print_info(){
		super.print_info();
		System.out.printf("major:%s\tclass:%s\n\n",major,classes);
	}
}
