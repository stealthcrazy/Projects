
public class Sponge {
	String hexResult = "";
	Sponge(int r , String N, String bits , int d ){
		String binN = binStringSP(N)+bits ;
		binN = new StringBuilder(binN).reverse().toString();
		
		State S  = new State();
		//System.out.println(binN);
		String P =Pad10(r,binN.length())+ binN ;
		P = flip8chunks(P);
		//System.out.println(P);
		int n  = P.length()/r;
		//System.out.println(n);
		int c = 1600 - r;
		
			
			String[] Ps = new String[n];
			int k = 0;
			for(int i = 0 ; i<n;i++) {
				Ps[i] = P.substring(k,k+r);
				k+=r;
				//System.out.println(Ps[i]);
				
			}
			
			String Z ="";
			for (int j = 0 ; j<n;j++) {
				
				
				
					State T = new State(Ps[j]+"0".repeat(c));
					S = Keccak.Keccak_f( State.XorStates(T, S),24  );
					
					
				
				
				
				
				
			}
			boolean flag = true;
			while(flag){
				Z+=S.displayStateString().substring(0,r/4);
				if (d<=(Z.length()*4)) {
					this.hexResult +=  Z.substring(0,d/4);
					flag = false;
				}else {
					S = Keccak.Keccak_f( S,24  );
				}
				
				
			}
			
		
		
		
		
		System.out.println(this.hexResult);
		
		
		
		
		
		
	}
	String binString(String S) {
		String BinString = "";
		
		for (int i = 0 ; i <S.length();i++) {
			String s = "";
			int k = ((int) S.charAt(i));
			//System.out.println(k);
			int pad = 0;
			if (Integer.toBinaryString(k).length() !=8) {
				pad = 8-Long.toBinaryString(k).length();
				//System.out.println(pad);
				s = "0".repeat(pad) +Integer.toBinaryString(k);
			}
			if (Long.toBinaryString(k).length() ==8) {
				pad = 0 ;
				s = ("0".repeat(pad) +Long.toBinaryString(k)).substring(0,8);
			}
			
			//System.out.println(s);
			BinString+=s;
			
		}
		//System.out.println();
		return BinString;
	}
	String binStringSP(String S) {
		String BinString = "";
		
		for (int i = 0 ; i <S.length();i++) {
			String s = "";
			int k = ((int) S.charAt(i));
			//System.out.println(k);
			s = Integer.toBinaryString(k);
			
			//System.out.println(s);
			BinString+=s;
			
		}
		//System.out.println();
		return BinString;
	}
	
	String Pad10(int x  , int m) {
		int j = (-m-2)%x;
		if (j <0) {
			j = x+j;
		}
		
		String P ="1"+ ("0".repeat(j))+"1";
		
		return P;
	}
	String flip8chunks(String x) {
		//System.out.println();
		String[] A = new String[(x.length()/8)];
		String R = "";
		int k =0;
		for (int i =0;i<(x.length()/8);i++) {
			A[i] = x.substring(k,k+8);
			k+=8;
		}
		
		for (int j =A.length-1;j>=0;j--) {
			//System.out.println(j);
			R+=A[j];
		}
		return R;
		
			
		
				
	}
	
	
}
