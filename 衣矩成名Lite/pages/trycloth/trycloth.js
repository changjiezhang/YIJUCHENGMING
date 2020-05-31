// pages/trycloth/trycloth.js
//获取全局变量
var app = getApp();
//var processed_img_url;
var img_src;
//touches的数组；
var touchs_corodernate = new Array()
Page({

  /**
   * 页面的初始数据
   */
  data: {
	  img_src:'',
	  touch:{
		  //distance:0,
		  scale:0.5,
		  baseWidth:null,
		  baseHeight:null,
		  scaleWidth:null,
		  scaleHeight:null
	  }
  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
	  console.log('hello')
	  //processed_img_url = app.globalData.processed_img_url;
	  //使用本地缓存传递处理后的数据,可以实现
	  wx.getStorage({
		key:'processed_img_url',
		success:res=>{
			console.log(res.data)
			this.setData({
				img_src:res.data
			})
		}
	  })
  },
  //touchmstart,小程序2.1.0暂时不支持 coverview暂时不支持，cover事件
  touchstartCallback:function(e){
    console.log(e)
	  /*if (e.touches.length==1) return
	  console.log('双手指开始运动')
	  console.log(e.touches)
	  let xMove = e.touches[1].clientX-e.touches[0].clientX;
	  console.log(xMove)
	  let yMove = e.touches[1].clientY-e.touches[0].clienty;
	  console.log(yMove)
	  let distance = Math.sqrt(xMove*xMove+yMove*yMove);
	  console.log(distance)
	  this.setData({
		  'touch.distance':distance,
	  })*/
    touchs_corodernate.push(e.touches[0])
  },
  //touch事件的使用
  touchmoveCallback:function(e){
    console.log(e)
		/*let touch = this.data.touch
		//单手缩放
		if(e.touches.length==1) return
			console.log("双手指运动")
			console.log(e.touches)
			let xMove = e.touches[1].clientX-e.touches[0].clientX;
			console.log(xMove)
			let yMove = e.touches[1].clientY-e.touches[0].clientY;
			console.log(yMove)
			//新的distance
			let distance = Math.sqrt(xMove*xMove+yMove*yMove);
			let distanceDiff = distance - touch.distance;
			let newScale = touch.scale + 0.005*distanceDiff
			console.log(newScale)
		//为了防止缩放得太大，scale需要限制，
		if(newScale >=2) {
			newScale =2
		}
		if(newScale <= 0.6){
			newScale =0.6
		}
		let scaleWidth = newScale * touch.baseWidth
		let scaleHeight = newScale * touch.baseHeight
		//赋值 新的=> 旧的
		this.setData({
			'touch.distance' : distance,
			'touch.scale' : newScale,
			'touch.scaleWidth':scaleWidth,
			'touch.scaleHeight':scaleHeight,
			'touch.diff':distanceDiff
		})*/
	},
  touchendCallback: function(e) {
      console.log(e)
    touchs_corodernate.push(e.changedTouches[0])
    console.log(touchs_corodernate)

    //计算变化的程度scale
    console.log(touchs_corodernate[1].clientY)
    console.log(touchs_corodernate[0].clientY)
    //使用y坐标模拟左右手缩放
    let yMove = touchs_corodernate[0].clientY - touchs_corodernate[1].clientY
    console.log(yMove)
    console.log(Math.abs(yMove))
    let newScale = this.data.touch.scale + 0.0005 * yMove
    if (newScale >= 2) {
      newScale = 2
    }
    if (newScale <= 0.4) {
      newScale = 0.4
    }
    console.log(newScale)
    let scaleWidth = newScale * this.data.touch.baseWidth
    console.log(scaleWidth)
    let scaleHeight = newScale * this.data.touch.baseHeight
    console.log(scaleHeight)
    //赋值 新的=> 旧的
    this.setData({
      //'touch.distance': distance,
      'touch.scale': newScale,
      'touch.scaleWidth': scaleWidth,
      'touch.scaleHeight': scaleHeight,
      //'touch.diff': distanceDiff
    })
    //console.log(this.data.touch.scaleHeight)
    //let yMove = touchs_corodernate[1].chientY-touchs_corodernate[0].chientY
    //let distance = sqrt(xMove*xMove+yMove*yMove)
    //这块计算出来距离后，其实可以直接乘以某一个系数，但是要累积的放大，就要记录原先的数据
    //这块要参考一下
    //let distanceDiff = distance - touch.distance;
    //let newScale = touch.scale + 0.005 * distanceDiff
    //需要将touchs_corodernate的清空,以备后用
    touchs_corodernate = new Array()
    console.log(touchs_corodernate)
  },
	//bindload 这个api是<image>组件的api类似<img>的onload属性
	bindload:function(e) {
    console.log(e)
		this.setData({
			'touch.baseWidth':e.detail.width,
			'touch.baseHeight':e.detail.height,
			'touch.scaleWidth':e.detail.width,
			'touch.scaleHeight':e.detail.height,
      'touch.scale': 0.5,
		})
	},
  
  /*
  backtochoose:function(){
	  wx.navigateTo({
					  url:'../index/index'
					})
  },*/
  // 切换相机前后置摄像头  
  devicePosition() {  
    this.setData({  
      device: !this.data.device,  
    })  
    console.log("当前相机摄像头为:", this.data.device ? "后置" : "前置");  
  }, 

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})