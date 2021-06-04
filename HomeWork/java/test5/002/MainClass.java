public class MainClass{
	public static void main(String args[]){
		Village zhaoZhuang, maJiaHeZi;
		zhaoZhuang=new Village("赵庄");
		maJiaHeZi=new Village("马家河子");
		zhaoZhuang.peopleNumber=100;
		maJiaHeZi.peopleNumber=100;
		Village.treeAmount=200;
		int leftTree=Village.treeAmount;
		System.out.println("森林中有 "+leftTree+" 颗树");
		zhaoZhuang.treePlanting(50);
		// leftTree=maJiaHeZi.lookTreeAmount();
		leftTree=Village.lookTreeAmount();
		System.out.println("森林中有 "+leftTree+" 颗树");
		maJiaHeZi.fellTree(70);
		leftTree=Village.lookTreeAmount();
		System.out.println("森林中有 "+leftTree+" 颗树");
		System.out.println("赵庄的人口:"+zhaoZhuang.peopleNumber);
		zhaoZhuang.addPeopleNumber(12);
		System.out.println("赵庄的人口:"+zhaoZhuang.peopleNumber);
		System.out.println("马家河子的人口"+maJiaHeZi.peopleNumber);
		maJiaHeZi.addPeopleNumber(10);
		System.out.println("马家河子的人口"+maJiaHeZi.peopleNumber);
	}
}
