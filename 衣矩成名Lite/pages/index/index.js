//index.js
var util = require('../../utils/util.js')

//var inidata ="请粘贴淘宝链接"
//淘宝链接字符串
var item_addr_text;
var imgUrls =[];
var imgUrl;
var images_hrefs=[];//tabbao img url list
//使用全局变量
var app = getApp();
var current_img_url = app.globalData.current_img_url;
var processed_img_url;
var current_item_id =0;
Page({
    data: {
        userInfo: {},
        logged: false,
        takeSession: false,
        requestResult: '',
		inputValue:'',
		imgUrls:[],
		indicatorDots: true, //小圆点显示
    },
	//获取输入的值,可以使用
	bindKeyInput: function (e) {
		item_addr_text = e.detail.value,
		console.log(item_addr_text)
	},
	//在这设置分享按钮
	onload:function(){
    wx.showShareMenu({
      
    })
	},
  //转发按钮
  onShareAppMessage:function(){
    return{
      title:'衣矩成名小程序',
      path:'pages/index/index',
      imgurl:'',
      success:function(res){
        //转发成功
        console.log("转发成功"+JSON.stringify(res));
      },
      fail:function(res){
        //转发失败
        console.log("转发失败"+JSON.stringify(res));
      }
    }
  },
	//解析淘宝链接,输入完成时进行淘宝链接解析
	gettaobaoIMG: function(){
			//显示加载页面
			wx.showLoading({
				title:'图像获取中',
			})
			wx.request({
				//url: "http://203.195.167.55:80/getTaobaoImg",//服务器地址,抓取淘宝图片
				url: "http://armirror.top/getTaobaoImg",//服务器地址,抓取淘宝图片
				method:'post',
				data: {
					 item_addr: item_addr_text ,
				  },
				header: {
					  'Content-Type': 'application/x-www-form-urlencoded' // 默认值
				},
				success:res=>{
					//获取成功后，取消loading 框的显示
					wx.hideLoading()
					//这块需要加入判断是不是空的
					images_hrefs= res.data
					console.log(images_hrefs)
				    if (images_hrefs =='not_find_imgurl'){
						this.setData({
							//注意imgUrls是个list
							imgUrls: ['/images/404_not_found.png'],
						})
					}
					else{
						//注意images_hrefs是string类型不是list
						images_hrefs= images_hrefs.replace('[','')
						images_hrefs= images_hrefs.replace(']','')
						//正则表达式去除所有的’单引号
						images_hrefs= images_hrefs.replace(/\'/g,'')
						images_hrefs=images_hrefs.split(',')
						console.log(images_hrefs)
						this.setData({
							imgUrls:images_hrefs,
						})
					}
			
				}							
			})		
	},
	//获取当前选择图片的imgurl
	getCurrentImgUrl:function(e){
		//var current_item_id;
		current_item_id= e.detail.current
		//current_img_url=images_hrefs[current_item_id]
		//console.log(current_img_url)
	},
	//处理选中的图片，并转到试衣服界面
	tryCloth:function(){
		//显示加载页面
			wx.showLoading({
				title:'图像处理中',
			})
		//当前展示图片的url
		current_img_url=images_hrefs[current_item_id]
		console.log(current_img_url)
		wx.request({
				//url: "http://203.195.167.55:80/getProcessdImg",//服务器地址，处理图片背景
				url: "http://armirror.top/getProcessdImg",//服务器地址，处理图片背景
				method:'post',
				data: {
					 img_url:current_img_url,
				  },
				header: {
					  'Content-Type': 'application/x-www-form-urlencoded' // 默认值
				},
				success:res=>{
					//获取成功后，取消loading 框的显示
					wx.hideLoading()
					processed_img_url= res.data
					console.log(typeof(processed_img_url))
					processed_img_url=processed_img_url.replace(/\'/g,'')
					console.log(typeof(processed_img_url))
					console.log(processed_img_url)
					//解析成功再跳转
					//使用本地缓存传递数据
					wx.setStorage({
						key: 'processed_img_url',
						data: processed_img_url
					}),
					wx.navigateTo({
					  url:'../trycloth/trycloth'
					})
				}							
			})
			//如果处理不成功的话，跳转没意义
		/*wx.navigateTo({
			url:'../trycloth/trycloth'
		})*/
	}
  
})
