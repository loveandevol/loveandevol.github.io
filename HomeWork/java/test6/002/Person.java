public class Person{
	String name;
	char sex;
	int age;
	Person(String name,char sex,int age){
		this.name=name;
		this.sex=sex;
		this.age=age;
	}
	void print_info(){
		System.out.printf("name:%s\tsex:%c\tage:%d\n\n",name,sex,age);
	}
}
