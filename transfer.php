<?php $file_path = "fan.txt";//txt格式默认用utf8格式，否则转换
$str=file_get_contents($file_path);
$encode= mb_detect_encoding($str, array('GB2312','GBK','UTF-8'),true);
if($encode=="GB2312")
{
    $str = iconv("GB2312","UTF-8",$str);
}
else if($encode=="GBK")
{
    $str = iconv("GBK","UTF-8",$str);
}
else if($encode=="EUC-CN")
{
    $str = iconv("GBK","UTF-8",$str);
}
else//CP936
{
    //$str = iconv("GB2312","UTF-8",$str);
    $str = mb_convert_encoding($str, 'UTF-8', 'GBK');//把GBK编码转化为 UTF-8编码
}
$arr=array();
for($i=0;$i<mb_strlen($str,'utf8');$i++){
    $arr[$i]=mb_substr($str,$i,1,'utf8');
    }
$imgpath = './08/';//图片保存的文件夹
foreach($arr as $key=>$value){
    $code=unicode_encode($value);
    if(file_exists($imgpath.$code.'.png')){
            echo $imgpath.$mycode.'.png is already exist';continue;
        }
    $value=urlencode($value);
    $url="http://sampler.linotype.com/sam/sam?ID=1390633^&text=".$value."^&sizex=4000^&sizey=4000^&fontsize=3000";
    $command="d:/wget/wget -T 25 -t 0 -O ".$imgpath.$code.".png ".$url;//d:/wget为wget的执行文件路径
exec($command);
    }
//将内容进行UNICODE编码，编码后的内容格式：56fe  
function unicode_encode($name)  
{  
    $name = iconv('UTF-8', 'UCS-2', $name);  
    $len = strlen($name);  
    $str = '';  
    for ($i = 0; $i < $len - 1; $i = $i + 2)  
    {  
        $c = $name[$i];  
        $c2 = $name[$i + 1];  
        if (ord($c) > 0)  
        {    // 两个字节的文字  
            $c=base_convert(ord($c), 10, 16);
            $c2=base_convert(ord($c2), 10, 16);
            if(strlen($c)<2)$c="0".$c;
            if(strlen($c2)<2)$c2="0".$c2;
            $str .=$c.$c2;   
        }  
        else  
        {  
            $str .= $c2;  
        }  
    }  
    return $str;  
} 