public class Employee{
	String name;
	String education;
	Employee(
			String name,
			String education)
	{
		this.name=name;
		this.education=education;
	}
	int print_info(){
		System.out.printf("\n姓名:%s\t教育:%s\n\n",name,education);
		return 0;
	}
}
