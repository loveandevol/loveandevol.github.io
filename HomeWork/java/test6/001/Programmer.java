public class Programmer extends Employee{
	String prog_language;
	String opera_system;
	String database;
	Programmer( String name, 
			String education,
			String prog_language,
			String opera_system,
			String database) {
		super(name,education);
		this.prog_language=prog_language;
		this.opera_system=opera_system;
		this.database=database;
	}
	public int print_info(){
		super.print_info();
		System.out.printf("\n编程语言:%s\t操作系统:%s\t数据库:%s\n\n",
				prog_language,opera_system,database);
		return 0;
	}
}
