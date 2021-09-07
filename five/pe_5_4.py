def new_password(oldpassword, newpassword):
    """
    Takes the old password and the new password as inputs. Returns True if the new password is accepted. The new
    password will be rejected when it's the same as the old password; it's shorter than 6 characters; it doesn't
    contain a number. returns False when rejected.
    """
    if newpassword != oldpassword:
        if len(newpassword) > 5:
            for char in newpassword:
                if char in '1234567890':
                    return True
    return False

print(new_password('kittens1', 'kittens1'))