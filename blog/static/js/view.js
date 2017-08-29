var n = {{ post.next }};
var p = {{ post.prev }};
var next = '<-';
var prev = '->';
document.getElementsByClass('views').innerHTML=next;
if (n=='t'){
  document.getElementById('next-a').innerHTML=next;
}
if (p=='t') {
  document.getElementById('prev-a').innerHTML=prev;
}
