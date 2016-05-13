from __future__ import unicode_literals, print_function

import spacy.en
import spacy.matcher
from spacy.attrs import ORTH, TAG, LOWER, IS_ALPHA, FLAG63

import plac


def main():
    nlp = spacy.en.English()
    example = u'''
Japanese telecom SoftBank and Alibaba announced a partnership on Friday to launch cloud computing services in Japan based on Alibaba Cloud.

According to the announcement, the cloud services will be offered out of SB Cloud Corporation, or SB Cloud, which will open a new data center in Japan. SoftBank's parent company is a major shareholder of Alibaba Group.

The joint venture will provide public cloud services from Alibaba Cloud to a range of companies, and allow Alibaba to extend its reach with access to SoftBank's business customer base in Japan, a country which is ranked 2nd among the top markets for global cloud services according to a recent report by the International Trade Administration. Gartner predicts that by 2018 the Asia Pacific and Japan region will account for $11.5 billion in total cloud services spending.

SB Cloud CEO and executive vice president of SoftBank Eric Gan said that the companies have been working on the joint venture over the "past few months."

SB Cloud's offerings will include data storage and processing services, enterprise-level middle as well as cloud security services, according to an announcement.

"We are proud that Alibaba Cloud can leverage its cloud computing expertise in the joint venture with SoftBank," Sicheng Yu, vice president of Alibaba Cloud said in a statement. "We look forward to helping more Japanese companies grow their business with our secure, scalable and innovative cloud computing services."

SB Cloud CEO and executive vice president of SoftBank Eric Gan said that the companies have been working on the joint venture over the "past few months."

Just last month, Digital Realty announced that it has pre-leased the entirety of its first Japan data center to a "major hyperscale cloud provider."
'''.strip()
    before = nlp(example)
    print("Before")
    for ent in before.ents:
        print(ent.text, ent.label_, [w.tag_ for w in ent])

if __name__ == '__main__':
    main()
    
