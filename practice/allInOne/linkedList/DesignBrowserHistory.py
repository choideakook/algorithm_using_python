# Browser History = url ( 수 : 1 ~ 20 / 길이 : 1 ~ 20 . 을 포함한 소문자)
# void visit = url 방문 ( 현재 page 앞의 모든 기록 삭제)
# string back = 뒤로가기 (int 타입인 step 수 만큼 이전 page 로 이동)
    # 뒤로가기가 완료되면 현제 URL 을 반환
# string forward = 앞으로 가기 (뒤로가기와 동일)
# step ( 1 ~ 100 )
# 호출 최대 5,000 번

class ListNode(object):
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.current = ListNode(val=homepage)

    def visit(self, url):
        self.current.next = ListNode(val=url, prev=self.current)
        self.current = (
        self.current.next)
        return None

    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.val

    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            self.current = self.current.next
        return self.current.val