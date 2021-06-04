class Village{
	static int treeAmount;
	int peopleNumber;
	String name;
	Village(String s){
		name=s;
	}
	void treePlanting(int n){
		treeAmount=treeAmount+n;
		System.out.println(name+"植树"+n+"颗");
	}
	void fellTree(int n){
		if(treeAmount-n>=n){
			treeAmount=treeAmount-n;
			System.out.println(name+"伐树"+n+"颗");
		}
		else{
			System.out.println("无木可伐");
		}
	}
	static int lookTreeAmount(){
		return treeAmount;
	}
	void addPeopleNumber(int n){
		peopleNumber=peopleNumber+n;
		System.out.println(name+"增加了"+n+"人");
	}
}
