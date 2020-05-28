<template>
    <el-form :model="Form" :rules="rules" ref="Form">
      <el-form-item label="用户名:" prop="username">
        <el-input v-model="Form.username" placeholder="初始用户名请输入学号" clearable></el-input>
      </el-form-item>
      <el-form-item label="电子邮箱:" prop="mail">
        <el-input v-model="Form.mail" placeholder="请输入可用邮箱" clearable></el-input>
        </el-form-item>
      <el-form-item label="密码:" prop="password">
        <el-input v-model="Form.password" placeholder="6-12位纯数字" show-password clearable auto-complete="off" oninput="value=value.replace(/^\.+|[^\d.]/g,'')"></el-input>
        </el-form-item>
        <el-form-item label="确认密码:" prop="checkpass">
          <el-input v-model="Form.checkpass" placeholder="6-12位纯数字" show-password clearable auto-complete="off" oninput="value=value.replace(/^\.+|[^\d.]/g,'')"></el-input>
          </el-form-item>
        <el-form-item>
          <el-button type = "primary" @click = "submitForm('Form')" style="width: 300px;">注册</el-button>
        </el-form-item>
    </el-form>
</template>

<script>
  import axios from 'axios';
  export default {
  	data() {
      var validatePass = (rule, value, callback) => {
      			if (value === '') {
      				callback(new Error('请输入密码'));
      			} else {
      				callback();
      			}
      		};
      var validatePass2 = (rule, value, callback) => {
      			if (value === '') {
      				callback(new Error('请再次输入密码'));
      			} else if (value !== this.Form.password) {
      				callback(new Error('两次输入密码不一致!'));
      			} else {
      				callback();
      			}
      		};


  		return {
        activeName: 'second',
        Form:{
          username:'',
          mail:'',
          password:'',
          checkpass:''
  		},
      rules: {
      				username: [{ required: true, message: '请输入您的学号', trigger: 'blur' }],
              mail: [{ required: true, type : 'email', message: '请输入您的可用邮箱', trigger: 'blur' }],
      				password: [{ required: true, validator: validatePass, trigger: 'blur' }],
      				checkpass: [{ required: true, validator: validatePass2, trigger: 'blur' }]
      			}

  	};
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
      	if (valid) {
      		const url = "/auth/register"
        axios.post(url, {
          'username': this.Form.username,
          'mail': this.Form.mail,
          'password': this.Form.password
        })
        .then(function (response) {
          console.log(response);
          if(parseInt(response.data.code) === 1){
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
  }
</script>
