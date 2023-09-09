package org.com.infocell.api.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.com.infocell.api.models.User;

public interface UserRepository extends JpaRepository<User, Integer>{}
