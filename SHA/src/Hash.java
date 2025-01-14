import java.util.ArrayList;

public class Hash {
	ArrayList<Long> a =  new ArrayList<Long>();
	ArrayList<Long> b =  new ArrayList<Long>();
	ArrayList<Long> c =  new ArrayList<Long>();
	ArrayList<Long> d =  new ArrayList<Long>();
	ArrayList<Long> e =  new ArrayList<Long>();
	ArrayList<Long> f =  new ArrayList<Long>();
	ArrayList<Long> g =  new ArrayList<Long>();
	ArrayList<Long> h =  new ArrayList<Long>();
	
	ArrayList<ArrayList<Long>> digest = new ArrayList<ArrayList<Long>>();
	
	
	
	Hash(Word w){
		GetInitialConstants SHA256_CONSTANTS = new  GetInitialConstants();
		
		ArrayList<ArrayList<Long>> W = w.Words;
		
		ArrayList<ArrayList<Long>> K = SHA256_CONSTANTS.KconstantArray;
		
		ArrayList<ArrayList<Long>> H = SHA256_CONSTANTS.HashConstantsArray;
		setIntialVariables(H);
		Compute(W, K);
		
		
		
		
		
		
		
		
	}
	void setIntialVariables(ArrayList<ArrayList<Long>> H) {
		
		this.a = H.get(0);
		this.b = H.get(1);
		this.c = H.get(2);
		this.d = H.get(3);
		this.e = H.get(4);
		this.f = H.get(5);
		this.g = H.get(6);
		this.h = H.get(7);
		
	}
	
	void Compute(ArrayList<ArrayList<Long>> W , ArrayList<ArrayList<Long>> K ) {
		
		for (int i = 0 ; i<64;i++) {
			
			//System.out.println(i);
			
			ArrayList<Long>  T1 =SigmaFunctions.add( SigmaFunctions.add(SigmaFunctions.add(SigmaFunctions.add(   this.h , SigmaFunctions.SigmaU2(this.e)    ) , SigmaFunctions.ChF(this.e, this.f, this.g)),K.get(i)),W.get(i));
			ArrayList<Long>  T2 = SigmaFunctions.add( SigmaFunctions.SigmaU1(this.a) , SigmaFunctions.MajF(this.a,this.b, this.c));
			
			ArrayList<Long> tempG= SigmaFunctions.duplicateArray(this.g);
			this.h.clear();
			this.h =tempG;
			
			ArrayList<Long> tempF= SigmaFunctions.duplicateArray(this.f);
			this.g.clear();
			this.g = tempF;
			
			ArrayList<Long> tempE = SigmaFunctions.duplicateArray(this.e);
			this.f.clear();
			this.f = tempE;
			
			
			this.e.clear();
			this.e = SigmaFunctions.add(this.d,T1);
			
			ArrayList<Long> tempC = SigmaFunctions.duplicateArray(this.c);
			this.d.clear();
			this.d = tempC;
			
			ArrayList<Long> tempB = SigmaFunctions.duplicateArray(this.b);
			this.c.clear();
			this.c = tempB;
			
			ArrayList<Long> tempA = SigmaFunctions.duplicateArray(this.a);
			this.b.clear();
			this.b =tempA;
			
			
			
			this.a.clear();	
			this.a = SigmaFunctions.add(T1,T2);
			
			
			
			
			
			
		
			
			
			
			
			
			
			
			
			
			
			
			
			
		}
		GetInitialConstants SHA256_CONSTANTSD = new  GetInitialConstants();
		ArrayList<ArrayList<Long>> H = SHA256_CONSTANTSD.HashConstantsArray;
		/*
		System.out.println(this.a);
		System.out.println(this.b);
		System.out.println(this.c);
		System.out.println(this.d);
		System.out.println(this.e);
		System.out.println(this.f);
		System.out.println(this.g);
		System.out.println(this.h);*/
		
		this.a = SigmaFunctions.add(this.a,H.get(0));
		this.b = SigmaFunctions.add(this.b,H.get(1));
		this.c = SigmaFunctions.add(this.c,H.get(2));
		this.d = SigmaFunctions.add(this.d,H.get(3));
		this.e = SigmaFunctions.add(this.e,H.get(4));
		this.f = SigmaFunctions.add(this.f,H.get(5));
		this.g = SigmaFunctions.add(this.g,H.get(6));
		this.h = SigmaFunctions.add(this.h,H.get(7));
		
		this.digest.add(this.a);
		this.digest.add(this.b);
		this.digest.add(this.c);
		this.digest.add(this.d);
		this.digest.add(this.e);
		this.digest.add(this.f);
		this.digest.add(this.g);
		this.digest.add(this.h);
		
		
		
		
		
		
		
		
	}
	
	
	

}
