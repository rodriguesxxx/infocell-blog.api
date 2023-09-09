package org.com.infocell.api.services;

import java.util.List;

import org.com.infocell.api.models.User;
import org.com.infocell.api.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;


@Service
public class UserService {
    
    @Autowired
    UserRepository userRepository;

    public List<User> list(){
        return userRepository.findAll();
    }

    public void add(User user){
        userRepository.save(user);
    }
}
