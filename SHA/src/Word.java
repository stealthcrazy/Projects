import java.util.ArrayList;

public class Word {
	ArrayList<ArrayList<Long>> Words = new ArrayList<ArrayList<Long>>();
	Word(String msg){
		createInitialWord(msg);
		msgSchedule();
	}
	
	void createInitialWord(String m) {
		PadMsg padM = new PadMsg(m);
		//System.out.println();
		
		//System.out.println(padM.PaddedMsg);
		int k = 0;
		for(int i  = 0 ; i< padM.PaddedMsg.size()/32;i++ ) {
			ArrayList<Long> word = new ArrayList<Long>();
			for(int j  = 0 ; j<32;j++ ) {
				
				word.add(padM.PaddedMsg.get(k));
				k+=1;
			}
			
			this.Words.add(word);
			
			
			
			
		}
	
	}
	void msgSchedule() {
		for(int i =16;i<64;i++) {
			
			ArrayList<Long> newWord  =  SigmaFunctions.add(SigmaFunctions.add( SigmaFunctions.add( SigmaFunctions.SigmaL2(this.Words.get(i-2)) ,this.Words.get(i-7) ) , SigmaFunctions.SigmaL1(this.Words.get(i-15)) ) , this.Words.get(i-16) ) ;
			//System.out.println(newWord);
			
			
			
			this.Words.add(newWord);
			
			
			
			//System.out.println(i);
			
			
		}
			
	}
}
