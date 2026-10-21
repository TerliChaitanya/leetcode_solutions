class ATM {
    int[] notes={0,0,0,0,0};
    int[] value={20,50,100,200,500};  
    public ATM() {
      
    }
    
    public void deposit(int[] banknotesCount) {
        for(int i=0;i<banknotesCount.length;i++){
            notes[i]+=banknotesCount[i];
        }
    }
    
    public int[] withdraw(int amount) {
        int [] result={0,0,0,0,0};
        int ramount=amount;
        
        for(int i=4;i>=0;i--){
            int n=ramount/value[i];
            int take=Math.min(n,notes[i]);
            
            result[i]=take;
            ramount-=take*value[i];
        }
        
        if(ramount!=0){
            int[] fa={-1};
            return fa;
        }
        
        for(int i=0;i<5;i++){
            notes[i]-=result[i];
        }
        
        return result;
    }
}

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */

/**
 * Your ATM object will be instantiated and called as such:
 * ATM obj = new ATM();
 * obj.deposit(banknotesCount);
 * int[] param_2 = obj.withdraw(amount);
 */