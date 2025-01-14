import java.util.ArrayList;

public class GetInitialConstants {
	ArrayList<Long> KConstant = new ArrayList<Long>();
	ArrayList<Long> HashConstants = new ArrayList<Long>();
	
	ArrayList<ArrayList<Long>> KconstantArray = new  ArrayList<ArrayList<Long>>();
	ArrayList<ArrayList<Long>> HashConstantsArray = new  ArrayList<ArrayList<Long>>();
	
	
	GetInitialConstants(){
		GenKConstants();
		GenHashConstants();
		formatConstants();
		
	}
	void  formatConstants() {
		for(long i : this.KConstant) {
			this.KconstantArray.add(SigmaFunctions.getbitArray(i));
		}
		for(long j : this.HashConstants) {
			this.HashConstantsArray.add(SigmaFunctions.getbitArray(j));
		}
	}
	static long getFractionalBits(long n,String type) {
		double x = 0;
		if (type == "K") {
			x = Math.cbrt(n)-Math.floor(Math.cbrt(n));
		}
		if (type == "H") {
			x = Math.sqrt(n)-Math.floor(Math.sqrt(n));
		}
		
		long y  = (long) (x * Math.pow(2, 32));
		return y;
	}
	void GenKConstants() {
		GenPrime Primes = new GenPrime(64);
		//System.out.println(Primes.primes);
		long constant;
		for(Long i : Primes.primes) {
			constant  = getFractionalBits(i,"K");
			this.KConstant.add( constant);
			
			
		}
		
	}
	void GenHashConstants() {
		GenPrime Primes_ = new GenPrime(8);
		long constant;
		for(Long i : Primes_.primes) {
			constant  = getFractionalBits(i,"H");
			this.HashConstants.add( constant);
			
			
		}
		
	}
	void display(String Type) {
		ArrayList<String> a = new ArrayList<String>() ;
		if(Type == "K") {
			for(long i : this.KConstant) {
				a.add(Long.toHexString(i));
			}
		}
		if(Type == "H") {
			for(long i : this.HashConstants) {
				a.add(Long.toHexString(i));
			}
		}
		System.out.println(a);
		
		
		
		
		
		
	}
	
	
	
	 

}
