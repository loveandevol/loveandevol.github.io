class Cat extends Animal{
    Cat(){
        name="猫";
    }
    Cat(String s){
        name=s;
    }
    public void cry(){
        System.out.println("Maio~ Miao~");
    }
    public void climbUpTree(){
        System.out.println(name+"会爬树"); 
    }
}
