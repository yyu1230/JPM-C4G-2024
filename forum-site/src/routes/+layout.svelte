<style>
    nav {
      width: 100%;
      background-color: #333;
    }
  
    ul {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 50px;
      list-style-type: none;
      margin: 0;
      padding: 0;
    }
  
    li {
      margin: 0 10px;
    }
  
    li a {
      color: white;
      text-decoration: none;
      padding: 14px 16px;
    }
  
    li a:hover {
      background-color: #111;
    }

    
  </style>
  
  <nav>
    <ul>
      <li><a href="/forum">Forum</a></li>
      <li><a href="/chat">Chat</a></li>
      <!--<li><a href="/videos">Videos</a></li>
      <li><a href="/profile">Profile</a></li>-->
    </ul>
  </nav>
  
  <slot></slot>