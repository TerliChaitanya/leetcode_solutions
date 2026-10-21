class ParkingSystem {
    int big;
    int small;
    int m;
    int[] p=new int[3];
    public ParkingSystem(int big, int medium, int small) {
        this.small=small;
        this.big=big;
        m=medium;
        p=new int[]{this.big,m,this.small};
    }
    
    public boolean addCar(int carType) {
        if(p[carType-1]>0){
            p[carType-1]-=1;
            return true;
        }
        return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */