from functools import total_ordering


@total_ordering
class Student:
    @staticmethod
    def _is_valid_operand(other):
        return (hasattr(other, 'firstname') and
                hasattr(other, 'lastname'))

    def __eq__(self, other):
        if not self._is_valid_operand(other):
            raise NotImplemented
        return ((self.firstname.lower(), self.lastname.lower()) ==
                (other.firstname.lower(), other.lastname.lower()))

    def __lt__(self, other):
        if not self._is_valid_operand(other):
            raise NotImplemented
        return ((self.firstname.lower(), self.lastname.lower()) <
                (other.firstname.lower(), other.lastname.lower()))
