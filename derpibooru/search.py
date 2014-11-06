# Copyright (c) 2014, Joshua Stone
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from .parameters import Parameters

class Search(Parameters):
  def __init__(self, q=[], page=1, perpage=15, comments=False, fav=False, key=""):
    Parameters.__init__(self, key, page, perpage, comments, fav)
    self.q = q

  @property
  def q(self):
    return(self.__q)

  @q.setter
  def q(self, q=[]):
    if not isinstance(q, list):
      raise TypeError("tags must be a list of strings")

    for tag in q:
      if not isinstance(tag, str):
        raise TypeError("{0} is not a string".format(tag))

      if "," in tag or tag == "":
        raise ValueError("tags can't contain commas or be empty strings")

    self.__q = [tag.strip() for tag in q]

  @property
  def url(self):
    parameters = []

    if self.q == []:
      search = "/images/page/{0}.json".format(self.page)
    else:
      search, tags = "/search.json", ",".join(self.q)
      parameters.append("q={0}".format(tags.replace(" ", "+")))
      parameters.append("page={0}".format(self.page))

    if self.comments == True:
      parameters.append("comments=")

    if self.fav == True:
      parameters.append("fav=")

    parameters.append("perpage={0}".format(self.perpage))

    url = (self.hostname + search)

    if parameters != []:
      url += "?{0}".format("&".join(parameters))

    return(url)

  @property
  def random(self):
    if not self.q:
      url = "https://derpiboo.ru/images/random.json"
    else:
      url = "https://derpiboo.ru/search.json?random_image=y"

      tags = ",".join(self.q)

      url += "&q={0}".format(tags.replace(" ", "+"))

    return(url)
