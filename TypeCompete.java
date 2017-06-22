/*
某学校进行打字比赛，比赛主要考查选手在规定时间内正确输入的字数。
但问题是，如何确定每一个输入的字是否是正确的（即是否与原稿相同），
因为完全存在选手错字、漏字和增字的情况，如：原稿为“abcde”,打字内容为“abece”.
比较可靠的办法是计算打字内容与原稿的最大相似子序列的长度，
所谓最大相似子序列即两者相等的子序列种最大的那个，如前面例子中两者最大相似子序列的长度为“abce”，
长度为4，请设计程序计算两个字符串的最大相似子序列的长度！用java编写
*/

public class typecompete {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

        int count = 0;
		String a ="interneabct";
		String b ="returnabc";
		String tempstr="";
		int max = 0; //最大匹配个数
		char[] bb = b.toCharArray();
		int weizhi = 0, j = 0;
		for (int i = 0; i < b.length(); i++) {
			count=0;
			j = j + i;
			a ="interneabct";
			for (; j < b.length(); j++) {
				if (a.indexOf(bb[j])!=-1) {
					weizhi = a.indexOf(bb[j]);
					tempstr = a.substring(weizhi+1);
					a = tempstr;
					//System.out.println(a);
					count = count + 1;
				}
			}
			if(count > max) {
				max = count;
			}
			j = 0;
		}
		System.out.println(max);
	}

}
