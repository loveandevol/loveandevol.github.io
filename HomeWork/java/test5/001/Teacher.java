public class Teacher{
	int teacherType;
	public void speek(){
		if(teacherType==1){
			System.out.printf("课程内容:二次方程\n");
		}
		else if(teacherType==2){
			System.out.printf("课程内容:学唱五线普\n");
		}
	}
}
