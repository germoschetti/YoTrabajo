export class User {
  username:any;
  email:string;
  password:string;
  
  constructor(email:string, password:string, username?:any){
    
    this.email = email;
    this.password = password;
    this.username = username;
  }
}