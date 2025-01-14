import java.util.ArrayList;
// doesnt support message more than 512-64
public class PadMsg {
	ArrayList<Long> PaddedMsg = new ArrayList<Long>();
	
	long[] Msg ;
	PadMsg(String msg){
		this.PaddedMsg = createPadMsg(msg);
		
	 }
	 
	long[] convMSG(String msg){
		 int len = msg.length();
		 byte[] MSG_ = msg.getBytes();
		 long[] temp = new long[len];
		 int c = 0;
		 for(byte i: MSG_) {
			 
			 temp[c] = (long) i;
			 c+=1;
			 //System.out.println((long) i);
		 }
		return temp;
		 
		 
		 
	}
	long[] joinBitArray(long[] a1 , long[] a2) {
		int len = a1.length +a2.length;
		long[] temp = new long[len];
		int k = 0;
		for(long i : a1) {
			temp[k] = i;
			k+=1;
		}
		int m = k-1;
		for(long j : a1) {
			temp[m] = j;
			m+=1;
		}
		return temp;
	}
	ArrayList<Long> createPadMsg(String msg) {
		long[] a1 = convMSG(msg);
		long len = a1.length*8;
		long[] l1 = {len};
		ArrayList<Long> b1 = MiscFunctions.bitArray(l1);
		ArrayList<Long> b2 = MiscFunctions.bitArray(a1);
		//System.out.println(b2.size());
		b2.add(1l);
		//System.out.println(b2.size());
		//System.out.println(512-64-b2.size());
		final int size  = b2.size();
		for(int i = 0; i<(512-64-size);i++) {
			
			b2.add(0l);
			//System.out.println(i);
		}
		//System.out.println(b2.size());
		for(int j = 512-64; j<512-b1.size();j++) {
			b2.add(0l);
		}
		//System.out.println(b2.size());
		int t =0 ;
		for(int k = 512-b1.size(); k<512;k++) {
			b2.add(b1.get(t));
			t+=1;
		}
		return b2;
		
		 
	}
	 
	 
	 
	 
	
}
