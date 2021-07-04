/**
 *  file: index.js
 *  June 6,2021
 *  writen by Mr.Cheng
 *
 */

console.log("微信:clhb66\nQQ:1403326337\n邮箱:ceelia0@163.com");

function getinfo() {
    console.dir(navigator.language);
    console.dir(location.href);
    console.dir(location.hostname);
}

var myFavorSite = {
    linux: "https://wiki.archlinux.org/",
    FrontPage1: "https://templated.co",
    FrontPage2: "https://templatemo.com",
    FrontPage3: "https://startbootstrap.com",
    FrontPage4: "https://github.com/learning-zone/website-templates",
    FrontPage5: "https://colorlib.com",
    FrontPage6: "https://bootstrapmade.com",
    FrontPage7: "https://bootstraptaste.com",
    show: function() {
        console.dir(this);
    },
};

var myPersonalInfo = {
    name: "Chengliang",
    sex: "male",
    age: "18",
    height: "180cm",
    weight: ">120g",
    education: "undergraduate",
    show: function() {
        console.dir("姓名", this.name);
        console.dir("性别", this.sex);
        console.dir("年龄", this.age);
        console.dir("身高", this.height);
        console.dir("学历", this.education);
    }
};

//鼠标点击标题触发事件
var clickTitle = document.getElementById("hello");
clickTitle.onclick = function() {
    // TODO: a evnet
    alert("阿祖，收手吧");
}

//鼠标指针坐标
function MousePlace() {
    x = window.event.x;
    y = window.event.y;
    position.innerHTML = "X:" + x + "  " + "Y:" + y + "  ";
}
document.onmousemove = MousePlace;

var buttonGrub32 = document.getElementById("buttonGrub32")
buttonGrub32.onclick = function() {
    var grubText = document.getElementById("grubText")
    var text = document.createTextNode("grub-install --target=i386-pc /dev/你的磁盘")
    grubText.innerHTML = "";
    grubText.appendChild(text)
}
var buttonGrub64 = document.getElementById("buttonGrub64")
buttonGrub64.onclick = function() {
    var grubText = document.getElementById("grubText")
    var text = document.createTextNode("grub-install --target=x86_64-efi --efi-directory=esp --bootloader-id=GRUB")
    grubText.innerHTML = "";
    grubText.appendChild(text)
}