ó
ðÌï[c           @   s,  d  d l  Z  d  d l Z d  d l Z d  d l Z d Z d Z d Z d Z d Z d   Z	 d   Z
 d	   Z d
   Z d   Z e   e	   e   e d  e j d  e   e   d GHe d e d e d  Z e d e d e d  Z e d e d e d  Z e d e d e d  Z e d e d e d  Z e d e d  Z e d e d e d e d e d e d  Z e d e d e d  Z e d e d e d  Z e d e d e d  Z e d e d d  Z d Z e Z d Z d  Z e d! e d" Z  e d# Z! e d$ Z" e d% Z# e d& e d Z$ d' e d( Z% e j& e  e j& e  e j& e  e j& e  e j& e   e j& e!  e j& e"  e j& e#  e j& e$  e j& e%  e   e
   e   e d) e d*  e j d+  e   e j'   d S(,   iÿÿÿÿNs   [1;31ms   [1;32ms   [1;33ms   [1;36ms   [0mc          C   sñ   d }  d } d } d } d } d } d } xÀ t  d  D]² } t j d	  t j j d
 |  | t |   | | t |  | | t |  | | t |  | | t |  | | t |  | | t |  d  t j j   q7 Wd  S(   Ns   LOADING       s   OADING       Ls   ADING       LOs   DING       LOAs   ING       LOADs   NG       LOADIs   G       LOADINi(   g¹?s   [1;37m[[1;32m s    [1;37m][0m(   t   ranget   timet   sleept   syst   stdoutt   writet   lent   flush(   t   lt   ot   at   dt   it   nt   gt   s(    (    s   Encrypt_by_AnonyMass.pyt   loading   s    c          C   sQ  d }  d } d } d } d } d } d } d } d	 } d
 }	 d	 }
 xt  d  D]ú } t j d  t j j d |  | t |   | | t |  | | t |  | | t |  | | t |  | | t |  | | t |  | | t |  | | t |  |	 | t |	  |
 | t |
  d  t j j   qO Wd  S(   Ns   L s   A s   G s   I s     s   P s   R s   O s   S s   E iF   gìQ¸ë±?s   [37m[[1;36ms   [1;37m](   R    R   R   R   R   R   R   R   (   R   R
   R   R   R   t   pt   rR	   R   t   et   St   z(    (    s   Encrypt_by_AnonyMass.pyt   proses   s    Úc           C   s   t  j d  d  S(   Nt   clear(   t   ost   system(    (    (    s   Encrypt_by_AnonyMass.pyR   +   s    c         C   sM   xF |  d D]: } t  j j |  t  j j   t j t j   d  q Wd  S(   Ns   
gü©ñÒMb ?(   R   R   R   R   R   R   t   random(   t   bR
   (    (    s   Encrypt_by_AnonyMass.pyt   run.   s    c           C   s±   d GHt  d t d GHt  d t d GHt  d t d GHt  d t d	 GHt  d
 t d GHd GHt d t  d t d  t d t  d t d  t d t  d t d  d  S(   Nt    s   ____ ____ _____ _____  s    ____  ____s   |  | |  | |   | |   |  s   |     |   |s   |__| |  | |   | |   |  s   |___  |s   |  | |  | |   | |   |      s   | |s   |  | |  | |___| |   |  s   ____| |___|s   Author: s   AnonyMass aka Zhu Bai Lees   WA Me : s   +62 822-1588-5532s   Github: s   https://github.com/mzubaili(   t   mR   R   (    (    (    s   Encrypt_by_AnonyMass.pyt   logo4   s    s   welcome to my toolsi   R   s	   nama sc: s   title: s   hacked by: s   warna text hacked: s   warna background: sg   masukkan link background jika ada
contoh:"https://images.jpg"
jangan lupa pake tanda [0m"[1;31m: [0ms   pesan s   ketik s   <br>s    untuk enter/selang sebaris: s   warna text pesan: s   font face: s   ukuran font: s   .htmlt   ws   <html>
<head>
<title>sU  
</title>
<meta name="description" content="Script by Anon Sc tools">

 <script type="text/javascript">
TypingText = function(element, interval, cursor, finishedCallback) {
if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {
this.running = true;
return;
}
this.element = element;
this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });
this.interval = (typeof interval == "undefined" ? 100 : interval);
this.origText = this.element.innerHTML;
this.unparsedOrigText = this.origText;
this.cursor = (cursor ? cursor : "");
this.currentText = "";
this.currentChar = 0;
this.element.typingText = this;
if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;
TypingText.all.push(this);
this.running = false;
this.inTag = false;
this.tagBuffer = "";
this.inHTMLEntity = false;
this.HTMLEntityBuffer = "";
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll = function() {
for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
if(this.running) return;
if(typeof this.origText == "undefined") {
setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
return;
}
if(this.currentText == "") this.element.innerHTML = "";
if(this.currentChar < this.origText.length) {
if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {
this.tagBuffer = "<";
this.inTag = true;
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {
this.tagBuffer += ">";
this.inTag = false;
this.currentText += this.tagBuffer;
this.currentChar++;
this.run();
return;
} else if(this.inTag) {
this.tagBuffer += this.origText.charAt(this.currentChar);
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {
this.HTMLEntityBuffer = "&";
this.inHTMLEntity = true;
this.currentChar++;
this.run();
return;
} else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {
this.HTMLEntityBuffer += ";";
this.inHTMLEntity = false;
this.currentText += this.HTMLEntityBuffer;
this.currentChar++;
this.run();
return;
} else if(this.inHTMLEntity) {
this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);
this.currentChar++;
this.run();
return;
} else {
this.currentText += this.origText.charAt(this.currentChar);
}
this.element.innerHTML = this.currentText;
this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");
this.currentChar++;
setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
} else {
this.currentText = "";
this.currentChar = 0;
this.running = false;
this.finishedCallback();
}
}
</script>
</head>s+   
<style type="text/css">
body{
background: s    url(s   );
font-family: s   ;
font-size: s   px;
color: sT   ;
height: 100%;
widht: 100%;
}
Hacked {
font-family: serif;
font-size: 40px;
color: s2   ;
}
</style>
<br>
<br>
<center>
<Hacked>hacked by s;   </Hacked>
<br>
<br>
<br>
<p align="center" id="AnonyMass">
s   
<script type="text/javascript">/*<![CDATA[*/

new TypingText(document.getElementById("AnonyMass"),98, function(i){ var ar = new Array("|", " ", " ", " "); return " " +

ar[i.length % ar.length]; });


//Type out examples:

TypingText.runAll();

/*]]>*/</script>
<br>
<br>
</body>
</html>s   sc nya sudah selesaisC   
kalo scnya jelek lu edit sendiri aja ya :v
capek tau buat tools :vi   ((   R   R   R   R   R   t   ht   kt   cR   R   R   R   R   R   R   t	   raw_inputt   nst   tt   hbt   whbt   bgt   urlt   msgt   mct   fmt   smt   opent   anont   zbl1t   zbl2t   zbl3t   zbl4t   zbl5t   zbl6t   zbl7t   zbl8t   zbl9t   zbl10R   t   close(    (    (    s   Encrypt_by_AnonyMass.pyt   <module>   s   					
4\
