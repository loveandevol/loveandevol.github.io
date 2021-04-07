public class MainClass{
	public static void main(String args[]){
		Teacher zhang, wang;
		zhang=new Teacher();
		wang=new Teacher();
		zhang.teacherType=1;
		wang.teacherType=2;
		School MidSch=new School();
		MidSch.setTeacher(zhang,wang);
		MidSch.startMathLesson();
		MidSch.startmusicLesson();
	}
}
