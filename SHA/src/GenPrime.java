import java.util.ArrayList;

public class GenPrime {
	ArrayList<Long> primes = new ArrayList<Long>();
	GenPrime(int PrimeN){
		
		getPrimes(PrimeN);
		
	}
	
	
	
	
	void getPrimes(int Amt) {
		int P = 0;
		long count = 1;
		boolean flag  = false;
		boolean notFound = true;
		
		while (notFound) {
			count+=1;
			flag = checkIfPrime(count);
			//System.out.println((flag == true));
			if (flag == false){
				this.primes.add(count) ;
				//System.out.println(count);
				P+=1;
				
			}
			//System.out.println(P ==(Amt-1));
			if(P ==Amt) {
				notFound = false;
			}
			
			
			
		}
		
		
	}
	boolean checkIfPrime(long n) {
		boolean flag = false;
		for (long i = 1 ; i<= n ; i++) {
			/*System.out.print(n+ " ");
			System.out.print(i);
			System.out.println((n%i == 0));*/
			if ((i!=n) && ( i!=1) && (n%i == 0)){
				flag = true;
				return flag;
				
						
			}
				
		}
		return flag;
		
	}
	public String toString() {
		String s = "[";
		for(long i : this.primes){
			s+=i +",";
		}
		s+="]";
		return s;
	}
	
	
	
		
		
	
	
	
}
