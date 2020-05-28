<template>
<!--  <div class = "index"> -->
    <el-container>
       <el-aside width="1190px">
         Datamining
        </el-aside>
       <el-main>
         <div class="log">学生成绩分析</div>
          <el-tabs class="log_tabs" v-model="activeName" @tab-click="handleClick">
             <el-tab-pane label="登录" name="first">
               <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
                 <el-form-item label="用户名:" prop="username">
                   <el-input v-model="ruleForm.username" placeholder="请输入您的用户名" clearable ></el-input>
                 </el-form-item>
                 <el-form-item label="密码:" prop="password">
                   <el-input v-model="ruleForm.password" placeholder="请输入您的密码" show-password clearable auto-complete="off" oninput="value=value.replace(/^\.+|[^\d.]/g,'')"></el-input>
                   </el-form-item>
                   <el-form-item>
                     <el-button type = "primary" @click = "submitForm('ruleForm')" style="width: 300px;">登录</el-button>
                   </el-form-item>
               </el-form>
                </el-tab-pane>
               <el-tab-pane label="注册" name="second">
                 <register></register>
               </el-tab-pane>
           </el-tabs>
         </el-main>
     </el-container>
<!--     </div> -->
</template>

<script>
  import axios from 'axios';
  import register from '@/components/register'
  export default {
    data () {
      var validatePass = (rule, value, callback) => {
         if (value === '') {
          callback(new Error('请输入密码'));
         }
         else {
          callback();
         }
        };
      return {
        activeName: 'first',
        ruleForm:{
          username:'',
          password:''
        },
        rules: {
        				username: [
                  { required: true, message: '请输入您的学号', trigger: ['blur'] },
                  ],
        				password: [
                  { required: true,  validator: validatePass, trigger: 'blur' },
                  ]
        			}
      };
    },
    methods:{
      handleClick(tab, event) {
              console.log(tab, event);
            },
      submitForm(formName) {
        this.$refs[formName].validate(valid => {
        	if (valid) {
        		const url = "/auth/login"
          axios.post(url, {
            'username': this.ruleForm.username,
            'password': this.ruleForm.password
          })
          .then(function (response) {
                    console.log(response)
                    if(parseInt(response.data.code) === 1){
                      window.location.href = 'HelloWorld'
                    }
                    else{
                      alert(response.data.error)
                    }
                  })
          .catch(function (error) {
            console.log(error);
          });
        	}
          else {
        		console.log('error submit!!');
        		return false;
        	}
        });
      		}
    },
    components: {
    		register
    	}
  }
</script>

<style>
  html,body,#app,.el-container{
          padding: 0px;
          margin: 0px;
          height: 100%;
      }
  .el-aside {
    background-image: url(../../static/joao-silas-I_LgQ8JZFGE-unsplash.jpg);
    background-size: cover;
    color: #c6c6c6;
    text-align: center;
/*    line-height: 755px; */
    font-size: 0px;
  }
  .el-main {
    background-color: #ffffff;
    color: #ffffff;
    font-size: 35px;
    text-align: center;
/*    line-height: 95px; */
  }
  .log{
    margin-top: 20px;
    font-size: 35px;
    color: #2b5d86;
  }
  .log_tabs{
    margin-top: 50px;
  }
</style>
