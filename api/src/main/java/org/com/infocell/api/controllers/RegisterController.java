package org.com.infocell.api.controllers;

import org.com.infocell.api.models.User;
import org.com.infocell.api.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/register")
public class RegisterController {
    
    @Autowired
    UserService userService;

    @GetMapping
    public String list(){
        return userService.list().toString();
    }

    @PostMapping
    public String register(@RequestBody User user){
        userService.add(user);
        return  "";
    }

}
